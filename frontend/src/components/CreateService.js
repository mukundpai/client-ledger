import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CreateService = () => {
  const [serviceData, setServiceData] = useState({
    service_title: '',
    client_id: '',
    category_id: '',
    service_type_id: ''
  });

  const [services, setServices] = useState([]);

  useEffect(() => {
    fetchServices();
  }, []);

  const fetchServices = async () => {
    try {
      const response = await axios.get('/api/services');
      setServices(response.data);
    } catch (error) {
      console.error('Error fetching services:', error);
      alert('Error fetching services');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setServiceData({ ...serviceData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/services', serviceData);
      console.log('Service created:', response.data);
      alert('Service created successfully!');
      fetchServices(); // Fetch the updated list of services
    } catch (error) {
      console.error('Error creating service:', error);
      alert('Error creating service');
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="text-center text-3xl font-extrabold text-gray-900">Create New Service</h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="service_title" className="sr-only">Service Title</label>
              <input
                id="service_title"
                name="service_title"
                type="text"
                required
                value={serviceData.service_title}
                onChange={handleChange}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Service Title"
              />
            </div>
            <div>
              <label htmlFor="client_id" className="sr-only">Client ID</label>
              <input
                id="client_id"
                name="client_id"
                type="text"
                required
                value={serviceData.client_id}
                onChange={handleChange}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Client ID"
              />
            </div>
            <div>
              <label htmlFor="category_id" className="sr-only">Category ID</label>
              <input
                id="category_id"
                name="category_id"
                type="text"
                required
                value={serviceData.category_id}
                onChange={handleChange}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Category ID"
              />
            </div>
            <div>
              <label htmlFor="service_type_id" className="sr-only">Service Type ID</label>
              <input
                id="service_type_id"
                name="service_type_id"
                type="text"
                required
                value={serviceData.service_type_id}
                onChange={handleChange}
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Service Type ID"
              />
            </div>
          </div>
          <div>
            <button
              type="submit"
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Create Service
            </button>
          </div>
        </form>
        <div className="mt-8">
          <h3 className="text-lg font-medium text-gray-900">Existing Services</h3>
          <ul className="mt-4 space-y-2">
            {services.map((service) => (
              <li key={service.service_id} className="bg-white p-4 rounded-lg shadow-md">
                <p className="text-gray-700 font-bold">{service.service_title}</p>
                <p className="text-gray-500">Client ID: {service.client_id}</p>
                <p className="text-gray-500">Category ID: {service.category_id}</p>
                <p className="text-gray-500">Service Type ID: {service.service_type_id}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default CreateService;