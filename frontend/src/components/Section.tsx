import React from 'react';

interface SectionProps {
    title?: string;
    children: React.ReactNode;
    className?: string;
    variant?: 'default' | 'compact' | 'spacious';
}

export default function Section({ 
    title, 
    children, 
    className = '', 
    variant = 'default' 
}: SectionProps) {
    // バリアントに応じたスタイル設定（iPhone SE対応）
    const getVariantStyles = () => {
        switch (variant) {
            case 'compact':
                return 'p-2 xs:p-3 space-y-1 xs:space-y-2';
            case 'spacious':
                return 'p-4 xs:p-6 space-y-3 xs:space-y-4';
            default:
                return 'p-3 xs:p-4 space-y-2 xs:space-y-3';
        }
    };

    // レスポンシブな幅設定（iPhone SE対応）
    const responsiveWidth = 'w-full max-w-full xs:max-w-sm sm:min-w-80 sm:max-w-md md:max-w-lg lg:max-w-xl xl:max-w-2xl';
    
    // レスポンシブなタイトルサイズ（iPhone SE対応）
    const titleSize = 'text-base xs:text-lg sm:text-xl font-semibold text-gray-800';

    return (
        <div className={`
            ${responsiveWidth}
            ${getVariantStyles()}
            bg-white 
            border 
            border-gray-200 
            rounded-lg xs:rounded-xl 
            shadow-sm
            hover:shadow-md
            transition-shadow
            duration-200
            mx-4 xs:mx-0
            ${className}
        `}>
            {title && (
                <h2 className={`${titleSize} mb-1 xs:mb-2`}>
                    {title}
                </h2>
            )}
            <div className="w-full overflow-hidden">
                {children}
            </div>
        </div>
    );
}