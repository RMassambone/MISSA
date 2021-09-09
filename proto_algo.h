#ifndef PROTO_ALGO_H
#define PROTO_ALGO_H

/**
\file proto_algo.h Prototypes for algorithms in constrained stochastic optimization.
*/

#include <vector>

// Interface definition for stochastic optimization operators.
class stoc_opt_operator{

   public:      
	   
	   virtual void apply( double lambda, int index, std::vector< double > stoc_error, std::vector< double > & x ) = 0;
        
       virtual ~stoc_opt_operator( void ){}
};

// Interface definition for feasibility operators.
class feasibility_operator{

   public:

      virtual void apply( std::vector< double >& x ) = 0;

      virtual ~feasibility_operator( void ){}
};


#endif
