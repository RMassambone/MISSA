#ifndef FEAS_H
#define FEAS_H

/**
\file feas.h Describes feasibility operators.
*/

#include "proto_algo.h"
#include <vector>

// Projection onto box constraints
class proj_box : public feasibility_operator {

   public:

      proj_box( std::vector< double > lb, std::vector< double > ub );
      
	  void apply( std::vector< double > & x );

      ~proj_box( void ){};
      
	private:
	
		std::vector< double > lb_;
		std::vector< double > ub_;
};

#endif
