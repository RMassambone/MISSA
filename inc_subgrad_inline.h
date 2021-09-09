#ifndef INC_SUBGRAD_INLINE_H
#define INC_SUBGRAD_INLINE_H

/**
   \file inc_subgrad_inline.h It implements the incremental subgradient operator.
*/

#include <math.h>
#include <stdio.h>
#include <iostream>
#include "inc_subgrad.h"
#include "funcao_inline.h"

// Global variables
extern std::vector< std::vector< double > > A;
extern std::vector< double > b;
extern std::vector< double > omega;

///Initializes incremental subgradient operator.
/**
Construtor: This version considers the incremental stochastic subgradient method with subgradients calculated from the weighted component functions, or not. The choice is made according to the "mode" argument.
\param mode 0 --> No weighting of the component functions, 1 --> weighted component functions.
*/
inc_subgrad::inc_subgrad( int mode )
  : mode_( mode ),
    op_( create_op() )
{}

// It returns a pointer to the class residual_norm_one.
residual_norm_one * inc_subgrad::create_op( void )
{
   residual_norm_one * op;
   op = new residual_norm_one(A, b, omega);
   
   return( op );
}

/// Apply operator.
/**
\param lambda Stepsize;
\param index_chain Markov chain state representing the index some component function.
\param eps Stochastic error incurred in subgradient.
\param x Vector that will be updated.
*/

void inc_subgrad::apply( double lambda, int index_chain, std::vector< double > eps, std::vector< double > & x )
{
   
   std::vector< double > subgrad(x.size());
   
   if ( mode_ == 0 ){
	   op_->subgrad_parcel(x, subgrad, index_chain);
   }
   
   if ( mode_ == 1 ){
	   op_->subgrad_parcel_weighted(x, subgrad, index_chain);
   }
   
   for(int i = 0; i < x.size(); i++){
       x[i] = x[i] - lambda * (subgrad[i] + eps[i]);
   }
}

#endif
