// 型定義の集約ファイル
export * from './Todo';
export * from './Tag';

// 共通の型定義
export interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
}

export interface PaginationParams {
  page?: number;
  limit?: number;
  search?: string;
}
