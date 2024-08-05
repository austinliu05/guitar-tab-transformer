import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Home: React.FC = () => {
    return (
        <Container>
            <Row className="mt-5 text-center">
                <h1>Welcome to Guitar Tab Transformer!</h1>
            </Row>
            <Row className='mt-5'>
                <h2>About</h2>
                <p className='mt-4'>The final goal of this project is to create a Recurrent Neural Network capable of transforming any song (.mp3 file) into <a
                    href='https://www.perplexity.ai/search/what-are-guitar-tabs-pJADgdOlTz6KabGjnNobOg#0'
                    target="_blank"
                    rel="noopener noreferrer">guitar tabs</a>.
                    As my first machine learning project, I have decided to divide the project into incremental steps as shown below.</p>
            </Row>
            <Row className='mt-5'>
                <Col>
                    <h2>Timeline</h2>
                </Col>
            </Row>
            <Row className='my-5'>
                <Col>
                    <h2>Frustration</h2>
                </Col>
            </Row>
        </Container>
    );
};

export default Home;
