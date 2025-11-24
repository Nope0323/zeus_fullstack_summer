interface ProductCardProps {
    title: string;
    price: number;
    description: string;
    imageUrl: string;
    inStock: boolean;

}

function ProductCard({ title, price, description, imageUrl, inStock }: ProductCardProps) {
    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "16px",
                maxWidth: "300px",
                margin: "10px",
            }}
        >
            <img 
            src={imageUrl} 
            alt={title} 
            style={{ width: "100%", borderRadius: "8px" }} />
            <h3>{title}</h3>
            <p>{description}</p>
            <p style={{ color: "#666" }}>${description}</p>
            <p style={{ fontSize: 24, fontWeight: "bold", color:"#007dff" }}>
                {price}$
            </p>
            <p style={{ color: inStock ? "green" : "red" }}>
                {inStock ? "In Stock" : "Out of Stock"}
            </p>
        </div>
    );
}

export default ProductCard;