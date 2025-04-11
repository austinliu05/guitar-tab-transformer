import React from 'react';
import { Card } from 'react-bootstrap';

interface BlogTitleProps {
    title: string;
}

const BlogTitle: React.FC<BlogTitleProps> = ({ title }) => {
    return (
        <Card.Title className="mb-2">{title}</Card.Title>
    );
};

export default BlogTitle;
