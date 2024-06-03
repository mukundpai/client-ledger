import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './components/Home';
import Register from './components/Register';
import Login from './components/Login';
import CreateService from './components/CreateService';


const App = () => {
  return (
        <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/create-service" element={<CreateService />} />
                </Routes>
            </Layout>
        </Router>
  );
};

export default App;