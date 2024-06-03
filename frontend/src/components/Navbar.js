import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <Link to="/" className="text-white text-xl font-bold">CLIENT LEDGER</Link>
          </div>
          <div className="flex items-center space-x-4">
            <Link to="/register" className="text-gray-300 hover:text-white">Register</Link>
            <Link to="/login" className="text-gray-300 hover:text-white">Login</Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
