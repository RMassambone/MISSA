#include <sstream>                          // std::istringstream, std::ostringstream
#include <iostream>                         // std::cin, std::cerr, std::cout, std::ofstream, std::ios::bin
#include <stdlib.h>                         // exit()
#include <chrono>                           // std::chrono
#include <math.h>                           // pow
#include <stdio.h>                          // sprintf, fprintf
#include "MISSA_inline.h"                   // MISSA
#include "funcao_inline.h"                  // objective function and subgradients
#include "inc_subgrad_inline.h"             // incremental subgradient method
#include "markov_chain_inline.h"            // markov chains
#include "stochastic_errors_inline.h"       // stochastic erros
#include "feas_inline.h"                    // Projection

void error( int err )
{
   std::cerr << "Error: usage: missa <niters> <nchains> <nthreads>\n";
   exit( -err );
}

// Problem parameters
std::vector< std::vector< double > > A(7, std::vector< double >(20));
std::vector< double > b(7);
std::vector< double > omega(7);

int main( int argc, char **argv )
{
   if ( argc < 4 )
      error( 5 );

   std::istringstream istrstr( argv[ 1 ] );
   int niters;
   if ( !( istrstr >> niters ) )
      error( 1 );

   istrstr.clear();
   istrstr.str( argv[ 2 ] );
   unsigned nchains;
   if ( !( istrstr >> nchains ) )
      error( 2 );

   istrstr.clear();
   istrstr.str( argv[ 3 ] );
   unsigned nthreads;
   if ( !( istrstr >> nthreads ) )
      error( 3 );

   std::cout.setf( std::ios::scientific );
   std::cout.precision( 16 );

   // Problem data
   std::vector< std::vector< double > > P(7, std::vector< double >(7));
   std::vector< std::vector< double > > init_distributions(nchains, std::vector< double >(7));
   std::vector< double > lb(20);
   std::vector< double > ub(20);
   
   lb[0] = -1.0; lb[1] = -0.5; lb[2] = -1.5; lb[3] = -1.3; lb[4] = 0.0; lb[5] = 0.1; lb[6] = 0.3; lb[7] = -0.2; lb[8] = -1.0;
   lb[9] = 0.0; lb[10] = -0.25; lb[11] = -0.1; lb[12] = 0.3; lb[13] = 0.1; lb[14] = 0.0; lb[15] = -1.1; lb[16] = 0.35; lb[17] = 0.15;
   lb[18] = 0.0; lb[19] = -0.45;
   
   ub[0] = 2.0; ub[1] = 1.5; ub[2] = 2.3; ub[3] = 3.0; ub[4] = 2.0; ub[5] = 1.8; ub[6] = 2.25; ub[7] = 1.7; ub[8] = 1.5; ub[9] = 2.0;
   ub[10] = 2.8; ub[11] = 1.75; ub[12] = 2.35; ub[13] = 1.95; ub[14] = 2.0; ub[15] = 1.0; ub[16] = 2.5; ub[17] = 1.35; ub[18] = 2.0; 
   ub[19] = 3.0;
   
   // Projection
   proj_box proj_op(lb, ub);
   
   A[0][1] = 0.5; A[0][2] = 0.1; A[0][3] = 0.2; A[0][13] = 0.25; A[0][14] = 0.1;
   A[1][5] = 0.4; A[1][6] = 0.15; A[1][11] = 0.3; A[1][15] = 0.45; A[1][18] = 0.1; A[1][19] = 0.2;
   A[2][12] = 0.02; A[2][13] = 0.06;
   A[3][0] = 0.12; A[3][1] = 0.21; A[3][2] = 0.3; A[3][6] = 0.5; A[3][12] = 0.4; A[3][13] = 0.1; A[3][14] = 0.18; A[3][18] = 0.1; A[3][19] = 0.14;
   A[4][0] = 0.8; A[4][1] = 0.4; A[4][7] = 1.2; A[4][8] = 1.0; A[4][9] = 0.85; A[4][16] = 0.4; A[4][17] = 0.7; A[4][18] = 0.1;
   A[5][1] = 0.25; A[5][2] = 0.34; A[5][7] = 0.45; A[5][8] = 0.35; A[5][12] = 0.18; A[5][13] = 0.22;
   A[6][12] = 0.05; A[6][13] = 0.08;
   
   // Generating b
   std::uniform_real_distribution< double > unif_dist(-2.0, 4.0);
   int seed = 1111;
   std::vector< double > solution(20);
   std::default_random_engine generator(seed);
   for (int i = 0; i < solution.size(); i++){
	   solution[i] = unif_dist(generator);
   }
   proj_op.apply(solution);
   
   for (int i = 0; i < 7; i++){
	   b[i] = 0.0;
	   for (int j = 0; j < 20; j++)
		   b[i] = b[i] + A[i][j] * solution[j];
   }
   
   omega[0] = 1.206467661691806e-01; omega[1] = 1.293532338308740e-01; omega[2] = 4.353233830846722e-02; omega[3] = 2.064676616915874e-01;
   omega[4] = 2.129629629631081e-01; omega[5] = 2.037037037038425e-01; omega[6] = 8.333333333339010e-02;
   
   // Objective function
   residual_norm_one RN1(A,b,omega);
   
   // Transition probability matrix
   P[0][1] = 1.0; P[1][2] = 1.0; P[2][3] = 1.0; P[3][4] = 1.0; P[4][5] = 1.0; P[5][6] = 1.0; P[6][0] = 1.0;
   
   // Initial distrib.
   init_distributions[0][0] = 1.0;
   
   // Markov chains
   markov_chain MC(P, init_distributions[0]);
   
   // This parameter defines whether the weighting in the component function will be considered.
   // 0 --> no weighting of the component functions, 1 --> weighted component functions.
   int mode = 1;
   
   // Decision variable.
   std::vector< double > x(20);
   
   // Stochastic errors
   std::vector< std::vector< double > > eps(nchains, std::vector< double >( x.size() ));
   std::vector< int > agents(7);
   
   // Objective function values
   std::vector< double > RN1_vect;
   double obj;
   
   // Time
   double cpu_time;
   
   // Stepsize parameters
   double a = 2.5;
   double xi = 0.667;
   
   // Incremental stoc. cyclic sub. object.
   MISSA cyclic_op(x.size(), nchains, nthreads, mode);
   
   // Markov chains states.
   std::vector< int > cur_states( nchains );
   std::vector< int > next_states( nchains );
   
   // Stochastic errors
   seed = 123456;
   for (int j = 0; j < agents.size(); j++){
   	agents[j] = j;
   }
   shuffle (agents.begin(), agents.end(), std::default_random_engine(seed));
   
   for ( int test = 1; test < 7; test++ ){
	   
	   // Initial guess
	   for (int i = 0; i < x.size(); i++)
		   x[i] = 0.0;
	   proj_op.apply(x);
	   
	   // Object to get stochastic errors
	   stochastic_errors err_op( test, agents );
	   
	   // Initialize time
	   cpu_time = 0.0;
	   
	   // Initialize vector with objective function values
	   obj = RN1.eval(x);
	   RN1_vect.push_back(obj);
	   
	   for (int k = 0; k < niters; k++){
		   next_states[0] = MC.eval_MC_time(k, cur_states[0]);
		   err_op.get_error( k, next_states[0], eps[0] );
		   
		   // Starting iteration
		   auto iterstart( std::chrono::high_resolution_clock::now() );
		   
		   // Optimization step
		   cyclic_op.apply( a / pow(k + 1.0, xi), next_states, eps, x );
		   
		   // Projection
		   proj_op.apply(x);
		   
		   // Ending iteration
		   auto iterend( std::chrono::high_resolution_clock::now() );
		   
	       // Storing time
		   cpu_time = cpu_time + (iterend - iterstart).count() * 1e-9;
		   
		   // Storing objective value
		   obj = RN1.eval(x);
		   RN1_vect.push_back(obj);
		   
		   // Update Markov states
		   cur_states[0] = next_states[0];
	   }
	   
	   std::cout << "CPU TIME FOR TEST " << test << ": " << cpu_time << "\n";
	   
	   // Write objective values in a file.
	   char buffer [500];
	   int str = std::sprintf(buffer, "/home/objective_cyclic_test-%d.txt", test );
	   FILE * arq;
	   arq = std::fopen (buffer, "w" );
	   for(int i = 0; i < RN1_vect.size(); i++){
		   std::fprintf(arq, "%.16lf", RN1_vect[i] );
		   std::fprintf(arq, "\n");
	   }
	   std::fclose(arq);
	   RN1_vect.clear();      
   }
   
   return( 0 );

}
