#ifndef MISSA_H
#define MISSA_H

/**
\file MISSA.h Describes algorithm MISSA (Markovian Incremental Stochastic Subgradient Algorithm) -- Algorithm 1 of:
R. Massambone, E. F. Costa and E. S. Helou. A Markovian Incremental Stochastic Subgradient Algorithm. Submitted to IEEE Transactions On Automatic Control.
*/

#include <vector>
#include "inc_subgrad.h"

class MISSA {

   public: 
      // The constructor considers: dimension of the decision variable, number of Markov chains to be used, number of threads to run the subiterations and the mode defining objective function.
	  MISSA ( int n, unsigned int nchains, unsigned int nthreads, int mode );

	  void apply( double lambda, std::vector< int > values_chains, std::vector< std::vector< double > > eps, std::vector< double > & x );
 
      ~MISSA( void ); ///<Destructor.
 
   private:
      
      unsigned int nchains_;
      unsigned int nthreads_;
	  int mode_;
      std::vector< inc_subgrad * > const ops_; ///< Number of inc. subgradient operators (subiterations).
      std::vector< std::vector< double > * > const accus_; ///< Per-thread storage.
      
      std::vector< inc_subgrad * > create_ops( void );
      std::vector< std::vector< double > * > create_accus( unsigned n );
	  void run_subiterations( double lambda, int index_chain, std::vector< double > eps, unsigned first, unsigned n_str, std::vector< double > & accum, std::vector< double >  const & x );
};

#endif
