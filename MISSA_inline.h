#ifndef MISSA_INLINE_H
#define MISSA_INLINE_H

/**
   \file MISSA_inline.h It implements the Markovian Incremental Stochastic Subgradient Algorithm (MISSA).
*/

#include "MISSA.h"
#include "inc_subgrad_inline.h"
#include <thread>
#include <functional>
#include <vector>

// The constructor considers: dimension of the decision variable, number of Markov chains to be used, number of threads to run the subiterations and the mode defining objective function.
MISSA::MISSA( int n, unsigned int nchains, unsigned int nthreads, int mode )
   : nchains_( nchains ? nchains : 1),
     nthreads_( ( nthreads > nchains ) ? nchains : ( nthreads ? nthreads : 1 ) ),
     mode_( mode ),
     ops_( create_ops() ),
     accus_( create_accus( n ) )
{}

// This function returns a vector of pointers to inc_subgrad.
std::vector< inc_subgrad * > MISSA::create_ops( void )
{
   std::vector< inc_subgrad * > ops( nchains_ );
   
   for ( std::vector< inc_subgrad * >::size_type cur_chain( 0 ); cur_chain < nchains_; ++cur_chain){
	  ops[ cur_chain ] = new inc_subgrad( mode_ );
   }
   
   return( ops );
}

// It returns a vector, with n_threads entries, of pointers to std::vector< double > of size n = x.size().
std::vector< std::vector< double > * > MISSA::create_accus( unsigned n )
{
   std::vector< std::vector< double > * > accus( nthreads_ );
   for ( std::vector< std::vector< double > * >::size_type i( 0 ); i < nthreads_; ++i )
      accus[ i ] = new std::vector< double >( n );
   return( accus );
}

// Computes the Markovian incremental stochastic subgradient subiteration.
void MISSA::run_subiterations( double lambda, int index_chain, std::vector< double > eps, unsigned first_str, unsigned n_str, std::vector< double > & accum, std::vector< double >  const & x )
{
   unsigned past_last( first_str + n_str );
   std::vector< double > res;
   accum.assign(x.size(), 0.0);

   for ( unsigned cur_str( first_str ); cur_str < past_last; ++cur_str ){
      res = x;
      ops_[ cur_str ]->apply( lambda, index_chain, eps, res);
      for (unsigned int i = 0; i < accum.size(); i++)
        accum[i] += res[i];
   }
}

/// This function applies run_subiterations in each thread.
/**
\param lambda Stepzise.
\param values_chains Markov chain states
\param eps Stochastic errors incurred in subgradients
\param x Input/Output.
*/ 
void MISSA::apply(double lambda, std::vector< int > values_chains, std::vector< std::vector< double > > eps, std::vector< double > & x )
{
   std::vector< std::thread * > threads( nthreads_ );

   unsigned first_str( 0 );
   unsigned n_str;
   
   // Creates working threads:
   for ( unsigned cur_thread( 0 ); cur_thread < nthreads_; ++cur_thread ){
      
	  // If nchains = nthreads, then n_str = 1.
	  n_str = ( nchains_ / nthreads_ ) + ( cur_thread < ( nchains_ % nthreads_ ) ); 
      
	  threads[ cur_thread ] = new std::thread( &MISSA::run_subiterations,
                                               this,
											   lambda,
											   values_chains[ cur_thread ],
											   eps[ cur_thread ],
                                               first_str,
                                               n_str,
                                               std::ref( *( accus_[ cur_thread ] ) ),
                                               std::ref( x )
                                             );
      first_str += n_str;
   }

   // Waits for threads to complete:
   for ( unsigned cur_thread( 0 ); cur_thread < nthreads_; ++cur_thread ){
      if ( threads[ cur_thread ]->joinable() ){
		threads[ cur_thread ]->join();
      }
      delete threads[ cur_thread ];
   }

   // Completes averaging:
   x = *accus_[ 0 ];
   std::vector< double > aux;
   for ( unsigned cur_thread( 1 ); cur_thread < nthreads_; ++cur_thread ){
     aux = *accus_[ cur_thread ];
     for (unsigned int i = 0; i < x.size(); i++)
        x[i] += aux[i];
   }
   for (unsigned int i = 0; i < x.size(); i++)
     x[i] /= nchains_;
}

MISSA::~MISSA( void )
{
   
   for ( unsigned i( 0 ); i < nchains_; ++i )
      delete ops_[ i ];

   for ( unsigned i( 0 ); i < nthreads_; ++i )
      delete accus_[ i ];
}


#endif
