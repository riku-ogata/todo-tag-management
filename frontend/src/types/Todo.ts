// Todo type definition
export interface Todo {
    id: number;
    title: string;
    description?: string;
    completed: boolean;
    tags: string[];
    createdAt: string;
    updatedAt: string;
  }