interface InterfaceButtonProps {
    text: string;
    color?: string;
}
function Button({ text, color= 'blue' }: InterfaceButtonProps) {
    // console.log(props);
    // object destructuring хувьсагч ялгаж авч байгаа
    // const { Text, color } = props;
    return (
        <button
            style={{
                backgroundColor:color,
                color: "white",
                padding: "10px 20px",
                border: "none",
                borderRadius: "5px",
            }}
        >
            {text}
        </button>
    );
}
export default Button;