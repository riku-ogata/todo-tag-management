// @ts-nocheck
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import TopRouter from '@/routers/TopRouter';
import TodoRouter from '@/routers/TodoRouter';
import TagRouter from '@/routers/TagRouter';
import AuthRouter from '@/routers/AuthRouter';

export default function AppRoutes() {
  return (
    <Routes>
      {/* トップページ */}
      <Route path="/" element={<TopRouter />} />
      
      {/* Todo関連 */}
      <Route path="/todos/*" element={<TodoRouter />} />
      
      {/* Tag関連 */}
      <Route path="/tags/*" element={<TagRouter />} />
      
      {/* 認証関連 */}
      <Route path="/auth/*" element={<AuthRouter />} />
    </Routes>
  );
};
