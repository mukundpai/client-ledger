import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const handleRegister = () => {
    navigate('/register');
  };

  const handleLogin = () => {
    navigate('/login');
  };
  
  const handleCreateService = () => {
    navigate('/create-service');
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="text-center text-3xl font-extrabold text-gray-900">
            Welcome to Our Application
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Your one-stop solution for managing your tasks and projects efficiently.
          </p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="space-y-4">
            <button
              onClick={handleRegister}
              className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Register
            </button>
            <button
              onClick={handleLogin}
              className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
            >
              Login
            </button>
            <button
              onClick={handleCreateService}
              className="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Create New Service
            </button>
          </div>
        </div>
        <div className="mt-8 text-center">
          <h3 className="text-lg font-medium text-gray-900">Features</h3>
          <ul className="mt-4 space-y-2">
            <li className="text-gray-700">- Manage your tasks efficiently</li>
            <li className="text-gray-700">- Collaborate with your team</li>
            <li className="text-gray-700">- Get real-time updates</li>
            <li className="text-gray-700">- Track your progress</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Home;