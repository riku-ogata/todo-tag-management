// frontend/src/components/TodoList.tsx
// @ts-nocheck
import React, { useState, useEffect } from 'react';
import { apiService, Todo, Tag } from '@/services/api';

interface TodoListProps {
  onTodoUpdate?: () => void;
}

export default function TodoList({ onTodoUpdate }: TodoListProps) {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await apiService.getTodos();
      setTodos(data);
    } catch (err) {
      setError('Todoの取得に失敗しました');
      console.error('Error fetching todos:', err);
    } finally {
      setLoading(false);
    }
  };

  const toggleTodo = async (id: number, completed: boolean) => {
    try {
      await apiService.updateTodo(id, { completed: !completed });
      await fetchTodos();
      if (onTodoUpdate) onTodoUpdate();
    } catch (err) {
      setError('Todoの更新に失敗しました');
      console.error('Error updating todo:', err);
    }
  };

  const deleteTodo = async (id: number) => {
    if (!window.confirm('このTodoを削除しますか？')) {
      return;
    }

    try {
      await apiService.deleteTodo(id);
      await fetchTodos();
      if (onTodoUpdate) onTodoUpdate();
    } catch (err) {
      setError('Todoの削除に失敗しました');
      console.error('Error deleting todo:', err);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto p-5">
        <div className="text-center py-16">
          <div className="inline-block w-10 h-10 border-4 border-gray-200 border-t-blue-500 rounded-full animate-spin mb-5"></div>
          <p className="text-gray-600 text-lg">読み込み中...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-4xl mx-auto p-5">
        <div className="text-center py-10">
          <p className="text-red-500 text-lg mb-5">{error}</p>
          <button 
            onClick={fetchTodos} 
            className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg transition-colors duration-200"
          >
            再試行
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-5">
      {/* ヘッダー */}
      <div className="flex justify-between items-center mb-8 pb-4 border-b-2 border-gray-200">
        <h2 className="text-3xl font-bold text-gray-800">Todo一覧</h2>
        <p className="text-gray-500 text-sm">
          全{todos.length}件 (完了: {todos.filter(t => t.completed).length}件)
        </p>
      </div>

      {todos.length === 0 ? (
        <div className="text-center py-16">
          <p className="text-gray-500 text-lg mb-2">Todoがありません</p>
          <p className="text-gray-400">新しいTodoを作成してください</p>
        </div>
      ) : (
        <div className="space-y-6">
          {todos.map((todo) => (
            <div 
              key={todo.id} 
              className={`bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-lg transition-all duration-200 hover:-translate-y-1 ${
                todo.completed ? 'opacity-70 bg-gray-50' : ''
              }`}
            >
              <div className="flex justify-between items-start mb-4">
                <h3 className={`text-xl font-semibold flex-1 mr-4 ${
                  todo.completed ? 'line-through text-gray-400' : 'text-gray-800'
                }`}>
                  {todo.title}
                </h3>
                
                <div className="flex gap-3 items-center">
                  <button
                    onClick={() => toggleTodo(todo.id, todo.completed)}
                    className={`w-8 h-8 rounded-full border-2 flex items-center justify-center text-sm font-bold transition-all duration-200 hover:scale-110 ${
                      todo.completed 
                        ? 'bg-green-500 text-white border-green-500' 
                        : 'text-gray-500 border-gray-300 hover:border-green-500'
                    }`}
                  >
                    {todo.completed ? '✓' : '○'}
                  </button>
                  
                  <button
                    onClick={() => deleteTodo(todo.id)}
                    className="w-8 h-8 rounded-full border-2 border-red-500 text-red-500 flex items-center justify-center text-lg font-bold transition-all duration-200 hover:bg-red-500 hover:text-white hover:scale-110"
                  >
                    ×
                  </button>
                </div>
              </div>
              
              {todo.description && (
                <p className="text-gray-600 leading-relaxed mb-4">{todo.description}</p>
              )}
              
              {todo.tags && todo.tags.length > 0 && (
                <div className="flex flex-wrap gap-2 mb-4">
                  {todo.tags.map((tag) => (
                    <span
                      key={tag.id}
                      className="px-3 py-1 rounded-full text-white text-sm font-medium shadow-sm"
                      style={{ backgroundColor: tag.color }}
                    >
                      {tag.name}
                    </span>
                  ))}
                </div>
              )}
              
              <div className="flex gap-5 text-sm text-gray-500 pt-4 border-t border-gray-100">
                <span className="flex items-center">
                  <span className="mr-1">📅</span>
                  作成: {formatDate(todo.created_at)}
                </span>
                {todo.updated_at !== todo.created_at && (
                  <span className="flex items-center">
                    <span className="mr-1">🔄</span>
                    更新: {formatDate(todo.updated_at)}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
