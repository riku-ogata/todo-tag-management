// @ts-nocheck
import React from 'react';
import './App.css';
import TodoList from './components/TodoList';

function App() {
  return (
    <div className="App">
      {/* ヘッダー */}
      <header className="bg-white bg-opacity-10 backdrop-blur-lg px-5 py-8 text-center text-white border-b border-white border-opacity-20">
        <h1 className="text-4xl font-bold mb-4 drop-shadow-lg">
          Todo Tag Manager
        </h1>
        <p className="text-xl opacity-90 font-light">
          タスクを管理して、タグで整理しましょう
        </p>
      </header>
      
      {/* メインコンテンツ */}
      <main className="py-10 min-h-screen">
        <TodoList />
      </main>
    </div>
  );
}

export default App;