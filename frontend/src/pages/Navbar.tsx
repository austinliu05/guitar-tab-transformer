import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/CustomNavbar.scss'
import logo from '../assets/images/logo.png';

import { Navbar, Nav, Container } from 'react-bootstrap';

const CustomNavbar: React.FC = () => {
    return (
        <Navbar bg="dark" variant='dark' expand="lg">
            <Container>
                <Navbar.Brand href="home"><img src={logo} width='50' height='50' className="d-inline-block align-top rotated-logo"
                    alt="Guitar Tab Transformer logo" /></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                    <Nav.Link as={Link} to="/home">Home</Nav.Link>
                    <Nav.Link as={Link} to="/binary-classification">Binary Classification</Nav.Link>
                    <Nav.Link as={Link} to="/multiclass-classification">Multiclass Classification</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default CustomNavbar;
