import React from 'react';
import { Card } from 'react-bootstrap';

interface BlogParagraphProps {
    text: string;
}

const BlogParagraph: React.FC<BlogParagraphProps> = ({ text }) => {
    return (
        <Card.Text className="mb-4">{text}</Card.Text>
    );
};

export default BlogParagraph;
