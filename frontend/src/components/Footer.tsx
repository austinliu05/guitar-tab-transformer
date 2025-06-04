import React from "react";
import "../styles/Footer.scss";

const Footer: React.FC = () => {
    return (
        <footer className="footer">
            <div className="footer-container">
                <div className="footer-left">
                    <h3>Future Plans</h3>
                    <p>
                        In Progress...
                    </p>
                </div>
                <div className="footer-center">
                    <h3>Contact</h3>
                    <p>
                        Email: <a href="mailto:info@example.com">austin_f_liu@brown.edu</a>
                    </p>
                </div>
                <div className="footer-right">
                    <h3>Social Media</h3>
                    <div className="social-icons">
                        <a
                            href="https://www.linkedin.com/in/austin-liu-797877262/"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            <i className="fab fa-linkedin-in"></i>
                        </a>
                        <a
                            href="https://github.com/austinliu05"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            <i className="fab fa-github"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div className="footer-bottom">
                <p>&copy; 2024 Austin Liu. All rights reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;
