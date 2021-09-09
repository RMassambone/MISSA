#ifndef FEAS_INLINE_H
#define FEAS_INLINE_H

/**
\file feas_inline.h It implements feasibility operators.
*/

#include <math.h>
#include <stdio.h>
#include <iostream>
#include "feas.h"

/**
Constructor
\param lb Lower bounds.
\param lb Upper bounds.
*/
proj_box::proj_box( std::vector< double > lb, std::vector< double > ub )
: lb_( lb ), ub_( ub )
{}

/// Apply operator.
/**
\param x Vector we want to project onto the feasible set.
*/

void proj_box::apply( std::vector< double > & x )
{
   for(int i = 0; i < x.size(); i++){
       if ( x[i] < lb_[i] )
		   x[i] = lb_[i];
	   if ( x[i] > ub_[i] )
		   x[i] = ub_[i];
   }
}

#endif
