#ifndef MARKOV_CHAIN_H
#define MARKOV_CHAIN_H

/**
\file markov_chain.h It describes the markov chain simulations.
*/

#include <vector>

class markov_chain {

   public:

      markov_chain( std::vector< std::vector< double > > P, std::vector< double > init_dist ); ///<Constructor
      
      int eval_MC_time( int k, int cur_state );

      ~markov_chain( void ){}; ///<Destrutor.
      
	private:
	
	  std::vector< std::vector< double > > P_;
	  std::vector< double > init_dist_;
};

#endif
