#ifndef FUNCAO_INTERFACE_H
#define FUNCAO_INTERFACE_H

#include<vector>

// Abstract class for representing functions given by a sum of convex functions.
class sum_convex_functions{

   public:

      virtual double eval( const std::vector< double >& x ) const = 0;
      virtual void subgrad_parcel( const std::vector< double >& x, std::vector< double >& subgrad, int index ) const = 0;
      virtual void subgrad_parcel_weighted( const std::vector< double >& x, std::vector< double >& subgrad, int index ) const = 0;
      virtual ~sum_convex_functions( void ){};
};

/// Residual norm 1 of the linear system Ax = b (or the weighted version WAx = Wb).
class residual_norm_one : public sum_convex_functions{

   public:

      residual_norm_one( const std::vector< std::vector< double > >& A, const std::vector< double > & b, const std::vector< double > & omega );
      
      virtual double eval( const std::vector< double >& x ) const;
      virtual void subgrad_parcel( const std::vector< double >& x, std::vector< double >& subgrad, int index ) const;
      virtual void subgrad_parcel_weighted( const std::vector< double >& x, std::vector< double >& subgrad, int index ) const;

      virtual ~residual_norm_one( void ){};

   private:

      std::vector< std::vector< double > > A_;
      std::vector< double > b_;
      std::vector< double > omega_;

};

#endif
