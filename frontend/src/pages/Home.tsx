import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import Timeline from "../components/Timeline";
import guitarTabsImage from '../assets/images/guitar-tabs.png';

const Home: React.FC = () => {
    return (
        <Container>
            <Row className="mt-5 text-center">
                <h1>Welcome to Guitar Tab Transformer!</h1>
            </Row>
            <Row className='my-3'>
                <h2 className='mb-3'>About</h2>
                <p>The final goal of this project is to create a Recurrent Neural Network capable of transforming any song (.mp3 file) into <a
                    href='https://www.perplexity.ai/search/what-are-guitar-tabs-pJADgdOlTz6KabGjnNobOg#0'
                    target="_blank"
                    rel="noopener noreferrer">guitar tabs</a>.</p>
                <img alt='guitar-tabs' src={guitarTabsImage}></img>
                <p>To make the development process easier, I have decided to divide the project into several incremental steps.</p>
            </Row>
            <Row className='my-3'>
                <Col>
                    <h2 className='mb-3'>Timeline</h2>
                    <Timeline/>
                </Col>
            </Row>
            <Row className='mt-3 mb-4'>
                <Col>
                    <h2>Frustration</h2>
                    <p>This project stems from my passion for guitar. As an amateur, I don't have perfect pitch, so I'm not one to instantly pick up a song by ear. I rely heavily on online tablature to learn new pieces. However, the frequent paywalls and limitations became frustrating. Driven by this frustration and a desire to challenge my computer science skills, I decided to create this project as a solution.</p>
                </Col>
            </Row>
        </Container>
    );
};

export default Home;
