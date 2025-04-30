import React from 'react'
import '../styles/Timeline.scss'

interface TimelineItemProps {
    date: string;
    title: string;
    description: string;
    image: string;
}
const timelineData = [
    { 
        date: "03/2025", 
        title: "Starting from Square 1", 
        description: "After a brief hiatus following Summer 2024, I re-engaged with my passion project when Claude reached out in November 2024 with a similar idea and proposed a collaboration. Together, we have built a small database of guitar tabs and encoded them using dataGP files. In process of developing and building the model before tuning it to our needs.", 
        image: "" 
    },
    {
        date: "08/2024",
        title: "Advancing to Notehead Classification",
        description: "Currently working on creating a model to recognize noteheads and their relative positions in the staff line. Once I have completed this task, I can begin designing an algorithm to convert the processed music sheets into guitar tabs.",
        image: ""
    },
    {
        date: "07/2024",
        title: "Simple Binary/Multiclass Classification",
        description: "I developed a Convolutional Neural Network (CNN) to analyze music sheets. The model successfully identified whether an element was a note and classified it into its respective musical category.",
        image: ""
    },
    {
        date: "06/2024",
        title: "Building a Foundation",
        description: "I focused on deepening my understanding of Machine Learning by completing courses from MIT OpenCourseWare. This intensive study provided a solid foundation for my upcoming projects.\n Resources:",
        image: ""
    },
];

const TimelineItem: React.FC<TimelineItemProps> = ({ date, title, description }) => {
    return (
        <div className='timeline-item mb-5'>
            <div className='d-flex flex-row align-items-center'>
                <div className='timeline-date me-3'>
                    <h5 className='mb-0'>{date}</h5>
                </div>
                <div className='timeline-content p-3 rounded'>
                    <h5 className='fw-bold'>{title}</h5>
                    <p>{description}</p>
                </div>
            </div>
        </div>
    )
}
const Timeline: React.FC = () => {
    return (
        <div className='timeline'>
            {timelineData.map((item, index) => (
                <TimelineItem
                    key={index}
                    date={item.date}
                    title={item.title}
                    description={item.description}
                    image={item.image}
                />
            ))}
        </div>
    )
}

export default Timeline;