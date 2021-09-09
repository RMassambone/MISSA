#ifndef STOCHASTIC_ERRORS_H
#define STOCHASTIC_ERRORS_H

/**
\file stochastic_errors.h Describes stochastic errors incurred in subgradient evaluations.
*/

#include <vector>

class stochastic_errors {

   public:

      stochastic_errors ( int type, std::vector< int > shuffled_agents ); ///<Constructor
      
      void get_error( int k, int index_chain, std::vector< double > & eps );

      ~stochastic_errors( void ){}; ///<Destrutor.
      
   private:
	   
	   int type_;
	   std::vector< int > shuffled_agents_;
};

#endif
