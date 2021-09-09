#ifndef INC_SUBGRAD_H
#define INC_SUBGRAD_H

/**
\file inc_subgrad.h Describes the Markovian incremental stochastic subgradient operator.
*/

#include "proto_algo.h"
#include "funcao.h"
#include <vector>

// Stochastic optimization operator.
class inc_subgrad : public stoc_opt_operator {

   public:

      inc_subgrad( int mode ); ///<Constructor
      
	  void apply( double lambda, int index_chain, std::vector< double > stoc_error, std::vector< double > & x );

      ~inc_subgrad( void ){}; ///<Destructor.
      
	private:
	
	  int mode_;
	  residual_norm_one * const op_;
	  residual_norm_one * create_op( void );
};

#endif
