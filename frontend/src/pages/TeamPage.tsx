import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import '../styles/TeamPage.scss';

const teamMembers = [
    {
        name: "Austin Liu",
        school: "Brown University",
        bio: "Austin is a dual-degree student in Applied-Math Computer Science and Economics.",
        image: `${process.env.PUBLIC_URL}/assets/images/placeholder.png`
    },
    {
        name: "Claude Hu",
        school: "University of Virginia",
        bio: "Claude is currently a researcher specializing in NLP.",
        image: `${process.env.PUBLIC_URL}/assets/images/placeholder.png`
    }
];

const TeamPage: React.FC = () => {
    return (
        <div className="page-container">
            <Container className="team-container text-center py-5 flex-grow-1">
                <h1 className="mb-4">Meet the Team</h1>
                <Row className="justify-content-center">
                    {teamMembers.map((member, index) => (
                        <Col lg={4} md={6} sm={12} key={index} className="mb-4">
                            <Card className="shadow-lg">
                                {member.image ? (
                                    <Card.Img variant="top" src={member.image} className="team-image" />
                                ) : (
                                    <div className="team-placeholder">No Image Available</div>
                                )}
                                <Card.Body>
                                    <Card.Title>{member.name}</Card.Title>
                                    <Card.Subtitle className="mb-2 text-muted">{member.school}</Card.Subtitle>
                                    <Card.Text>{member.bio || "Bio coming soon..."}</Card.Text>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            </Container>
        </div>
    );
};

export default TeamPage;