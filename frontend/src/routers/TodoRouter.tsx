// @ts-nocheck
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Todo from '@/pages/todo/Index';

export default function TodoRouter() {
  return (
    <Routes>
      <Route path="/" element={<Todo />} />
    </Routes>
  );
}
