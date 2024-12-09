import React from 'react';
import { Card, Container } from 'react-bootstrap';
import BlogImage from '../components/BlogImage';
import BlogTitle from '../components/BlogTitle';
import BlogCaption from '../components/BlogCaption';
import BlogParagraph from '../components/BlogParagraph';

// Define the blog post data within the component
const NoteheadBlog: React.FC = () => {
    const post = {
        title: "Notehead Classification",
        imageSrc: "https://via.placeholder.com/800x400",
        imageAlt: "A placeholder image",
        caption: "A deep dive into Notehead Classification using AI",
        paragraphs: [
            "This is the first paragraph of the blog post about notehead classification.",
            "Here is the second paragraph with more technical details.",
            "Finally, this is the last paragraph with some closing thoughts."
        ]
    };

    return (
        <Container className="mt-4">
            <Card>
                <Card.Body>
                    <BlogTitle title={post.title} />
                    <BlogImage src={post.imageSrc} alt={post.imageAlt} />
                    <BlogCaption caption={post.caption} />
                    {post.paragraphs.map((paragraph, index) => (
                        <BlogParagraph key={index} text={paragraph} />
                    ))}
                </Card.Body>
            </Card>
        </Container>
    );
};

export default NoteheadBlog;
