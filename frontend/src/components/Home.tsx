import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';

const Home: React.FC = () => {
    return (
        <Container>
            <Row className="my-5">
                <Col>
                    <h1>Welcome to Guitar Tab Transformer</h1>
                    <p>This is a placeholder homepage.</p>
                </Col>
            </Row>
        </Container>
    );
};

export default Home;
