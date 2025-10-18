// frontend/src/services/api.ts
// @ts-nocheck

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export interface Todo {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  tags: Tag[];
  created_at: string;
  updated_at: string;
}

export interface Tag {
  id: number;
  name: string;
  color: string;
}

class ApiService {
  private baseUrl: string;

  constructor() {
    this.baseUrl = API_BASE_URL;
  }

  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    const config: RequestInit = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  // Todo関連のAPI
  async getTodos(): Promise<Todo[]> {
    return this.request<Todo[]>('/todos/');
  }

  async getTodo(id: number): Promise<Todo> {
    return this.request<Todo>(`/todos/${id}`);
  }

  async createTodo(todoData: {
    title: string;
    description?: string;
    completed?: boolean;
    tag_names?: string[];
  }): Promise<Todo> {
    const params = new URLSearchParams();
    params.append('title', todoData.title);
    if (todoData.description) params.append('description', todoData.description);
    if (todoData.completed !== undefined) params.append('completed', todoData.completed.toString());
    if (todoData.tag_names) {
      todoData.tag_names.forEach(tag => params.append('tag_names', tag));
    }

    return this.request<Todo>('/todos/', {
      method: 'POST',
      body: params,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
  }

  async updateTodo(id: number, todoData: Partial<Todo>): Promise<Todo> {
    return this.request<Todo>(`/todos/${id}`, {
      method: 'PUT',
      body: JSON.stringify(todoData),
    });
  }

  async deleteTodo(id: number): Promise<void> {
    return this.request<void>(`/todos/${id}`, {
      method: 'DELETE',
    });
  }
}

export const apiService = new ApiService();
