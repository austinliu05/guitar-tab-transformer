import React from 'react';
import { Card } from 'react-bootstrap';

interface BlogCaptionProps {
    caption: string;
}

const BlogCaption: React.FC<BlogCaptionProps> = ({ caption }) => {
    return (
        <Card.Subtitle className="mb-2 text-muted">{caption}</Card.Subtitle>
    );
};

export default BlogCaption;
