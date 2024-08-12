import React from 'react'

interface TimelineItemProps {
    date: string;
    title: string;
    description: string;
    image: string;
}
const timelineData = [
    {
        date: "06/2024",
        title: "Laying the Foundation",
        description: "I spent June deepening my understanding of Machine Learning by completing courses from MIT OpenCourseWare. This intensive study provided a solid foundation for my upcoming projects.",
        image: ""
    },
    {
        date: "07/2024",
        title: "Exploring Classification Techniques",
        description: "In July, I developed a Convolutional Neural Network (CNN) to analyze music sheets. The model successfully identified whether an element was a note and classified it into its respective category.",
        image: ""
    },
    {
        date: "08/2024",
        title: "Advancing to Multiclass Classification",
        description: "By August, I made significant progress towards the final product. I enhanced the CNN to not only identify notes but also determine their durations based on the notehead and stem. The model further classified notes based on their position within the staff and generalized its recognition to new music sheets found online.",
        image: ""
    },    
];

const TimelineItem: React.FC<TimelineItemProps> = ({date, title, description}) => {
    return (
        <div className='timeline-item mb-5'>
            <div className='d-flex flex-row align-items-center'> 
                <div className = 'timeline-date me-3'>
                    <h5 className='mb-0'>{date}</h5>
                </div>
                <div className='timeline-content bg-light p-3 rounded'>
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