// Type definitions for Todo Tag Manager
export interface Todo {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  tags: string[];
  createdAt: string;
  updatedAt: string;
}

export interface Tag {
  id: number;
  name: string;
  color?: string;
  createdAt: string;
}
