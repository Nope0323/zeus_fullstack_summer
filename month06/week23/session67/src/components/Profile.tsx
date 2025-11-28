import React from 'react';

interface ProfileProps {
    name: string;
    imgUrl: string;
    profession: string;
    age: number;
    width: number;
    height: number; 
}

// functional component
function Profile(props: ProfileProps) {
    return (
        <>
            <h1>{props.name}</h1>
            <img 
            width={props.width}
            height={props.height}
            src={props.imgUrl}/>
            <ul>Profession: {props.profession}</ul>  
            <ul>Age: {props.age}</ul>
            
        </>

    );
}

export default Profile;
