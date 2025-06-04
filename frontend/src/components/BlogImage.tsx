import React from 'react';
import { Image } from 'react-bootstrap';

interface BlogImageProps {
    src: string,
    alt: string,
}
const BlogImage: React.FC<BlogImageProps> = ({src, alt}) => {
    return (
        <Image src={src} alt={alt} fluid className="mb-4" />
    );
};

export default BlogImage;
