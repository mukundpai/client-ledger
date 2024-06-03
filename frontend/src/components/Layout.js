import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow container mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
      <footer className="bg-gray-800 py-4">
        <div className="text-center text-white">
          © 2024 Your Company. All rights reserved.
        </div>
      </footer>
    </div>
  );
};

export default Layout;
