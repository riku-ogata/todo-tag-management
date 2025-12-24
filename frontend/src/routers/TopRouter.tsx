// @ts-nocheck
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Top from '@/pages/top/Index';

export default function TopRouter() {
  return (
    <Routes>
      <Route path="/" element={<Top />} />
      <Route path="/top" element={<Top />} />
    </Routes>
  );
};
