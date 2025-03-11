import React from 'react';
import '../styles/TeamPage.scss';

const teamMembers = [
    {
        name: "Austin Chen",
        school: "Brown University",
        bio: "Austin is a dual-degree student in Applied-Math Computer Science and Economics with a passion for scalable software and AI-driven music transcription.",
        image: "../assets/images/austin.jpg"
    },
    {
        name: "Claude Hu",
        school: "Univeristy of Virginia",
        bio: "",
        image: ""
    }
];

const TeamPage: React.FC = () => {
    return (
        <div className="team-container">
            <h1>Meet the Team</h1>
            <div className="team-members">
                {teamMembers.map((member, index) => (
                    <div className="team-card" key={index}>
                        <img src={member.image} alt={member.name} className="team-image" />
                        <h2>{member.name}</h2>
                        <h3>{member.school}</h3>
                        <p>{member.bio}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TeamPage;
