import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/CustomNavbar.scss';
import logo from '../assets/images/logo.png';
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap';

const CustomNavbar: React.FC = () => {
    const location = useLocation();

    return (
        <Navbar bg="dark" variant='dark' expand="lg">
            <Container>
                <Navbar.Brand>
                    <img 
                        src={logo} 
                        width='50' 
                        height='50' 
                        className="d-inline-block align-top rotated-logo"
                        alt="Guitar Tab Transformer logo" 
                    />
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link 
                            as={Link} 
                            to="/" 
                            className={location.pathname === '/' ? "active-link" : ""}
                        >
                            Home
                        </Nav.Link>
                        <Nav.Link 
                            as={Link} 
                            to="/team" 
                            className={location.pathname === '/team' ? "active-link" : ""}
                        >
                            Team
                        </Nav.Link>
                        <NavDropdown title="Previous Works" id="previous-works-dropdown">
                            <NavDropdown.Item 
                                target="_blank" 
                                href='https://www.kaggle.com/code/apoxieforest/gtt-intro-preprocessing'
                            >
                                Preprocessing
                            </NavDropdown.Item>
                            <NavDropdown.Item 
                                target="_blank" 
                                href='https://www.kaggle.com/code/apoxieforest/gtt-binary-classification'
                            >
                                Binary Classification
                            </NavDropdown.Item>
                            <NavDropdown.Item 
                                target="_blank" 
                                href='https://www.kaggle.com/code/apoxieforest/gtt-multiclass-classification'
                            >
                                Multiclass Classification
                            </NavDropdown.Item>
                            <NavDropdown.Item 
                                target="_blank" 
                                href='https://www.kaggle.com/code/apoxieforest/gtt-note-identification'
                            >
                                Notehead Classification
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default CustomNavbar;