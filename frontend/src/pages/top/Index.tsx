// @ts-nocheck
import React, { useState } from 'react';
import Section from '@/components/Section';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Index() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // ナビゲーションを使用

  // ログイン処理
  const handleLogin = (e: React.FormEvent<HTMLFormElement>) => {
    // e.preventDefault();
    // axios.post('http://localhost:8000/api/login', { email, password })
    //   .then(response => {
    //     if (response.status === 200) {
    //       localStorage.setItem('token', response.data.token);
    //       navigate('/todos');
    //     } else {
    //       alert(response.data.message);
    //     }
    //   })
    //   .catch(error => {
    //     console.error('ログインに失敗しました', error);
    //   });
    navigate('/todos');
  };

  return (
    <div className='w-full h-full'>
      <div className='flex items-center justify-center h-screen'>
        {/* ログインフォーム */}
        <Section title="ログイン">
          <form onSubmit={handleLogin} className='w-full space-y-2'>
            {/* メールアドレス入力フォーム */}
            <div className='flex items-center border border-gray-200 rounded-md p-2'>
              <input
                type="text"
                placeholder='メールアドレス'
                className='w-full outline-none'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            {/* パスワード入力フォーム */}
            <div className='flex items-center border border-gray-200 rounded-md p-2'>
              <input
                type="password"
                placeholder='パスワード'
                className='w-full outline-none'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            {/* ログインボタン */}
            <div className='flex items-center justify-center py-2'>
              <button type='submit' className='bg-blue-500 hover:bg-blue-400 text-white px-4 py-2 rounded-md'>ログイン</button>
            </div>
          </form>
        </Section>
      </div>
    </div>
  );
}