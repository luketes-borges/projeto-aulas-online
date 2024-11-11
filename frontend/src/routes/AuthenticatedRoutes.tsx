import React from 'react';
import { Routes, Route } from 'react-router-dom';
import PrivateRoute from './PrivateRoute';
import Aulas from '../components/Aulas';
import AulaForm from '../components/AulaForm';
import Perfil from '../components/Perfil';
import DashboardInstrutor from '../components/DashboardInstrutor';

const AuthenticatedRoutes: React.FC = () => {
  return (
    <Routes>
      <Route element={<PrivateRoute />}>
        <Route path="/" element={<Aulas />} />
        <Route path="/aulas/criar" element={<AulaForm />} />
        <Route path="/aulas/:id/editar" element={<AulaForm />} />
        <Route path="/perfil" element={<Perfil />} />
        <Route path="/dashboard-instrutor" element={<DashboardInstrutor />} />
      </Route>
    </Routes>
  );
};

export default AuthenticatedRoutes;
