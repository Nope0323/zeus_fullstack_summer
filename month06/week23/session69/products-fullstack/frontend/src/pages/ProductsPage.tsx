import { useState, useEffect } from "react";
import type { Product, Category, ProductStats } from "../types";
import { getProducts, getCategories, getProductStats } from "../services/api";

import ProductList from "../components/ProductList";
import CategoryFilter from "../components/CategoryFilter";
import SearchBar from "../components/SearchBar";

const ProductsPage = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [stats, setStats] = useState<ProductStats | null>(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [selectedCategory, setSelectedCategory] = useState<number | null>(null);
  const [searchQuery, setSearchQuery] = useState("");

  // Fetch categories & stats
  useEffect(() => {
    const fetchInitial = async () => {
      try {
        const [categoriesData, statsData] = await Promise.all([
          getCategories(),
          getProductStats(),
        ]);
        setCategories(categoriesData);
        setStats(statsData);
      } catch (e) {
        console.error("Initial fetch error:", e);
      }
    };

    fetchInitial();
  }, []);

  // Fetch products when filters change
  useEffect(() => {
    const fetchProductsData = async () => {
      setLoading(true);
      setError(null);

      try {
        const data = await getProducts({
          category: selectedCategory ?? undefined,
          search: searchQuery || undefined,
        });
        setProducts(data);
      } catch (e) {
        setError("Бүтээгдэхүүнүүдийг ачаалахад алдаа гарлаа");
        console.error("Products fetch error:", e);
      } finally {
        setLoading(false);
      }
    };

    fetchProductsData();
  }, [selectedCategory, searchQuery]);

  return (
    <div className="products-page">
      <header className="page-header">
        <h1>Бүтээгдэхүүнүүд</h1>

        {stats && (
          <div className="stats-bar">
            <div className="stat-item">
              <span className="stat-value">{stats.total_products}</span>
              <span className="stat-label">Нийт</span>
            </div>

            <div className="stat-item">
              <span className="stat-value">{stats.active_products}</span>
              <span className="stat-label">Идэвхтэй</span>
            </div>

            <div className="stat-item">
              <span className="stat-value">{stats.total_categories}</span>
              <span className="stat-label">Ангилал</span>
            </div>

            <div className="stat-item">
              <span className="stat-value">{stats.out_of_stock}</span>
              <span className="stat-label">Дууссан</span>
            </div>
          </div>
        )}
      </header>

      <div className="page-content">
        <aside className="sidebar">
          <SearchBar onSearch={setSearchQuery} />
          <CategoryFilter
            categories={categories}
            selectedCategory={selectedCategory}
            onSelectCategory={setSelectedCategory}
          />
        </aside>

        <main className="main-content">
          <div className="results-info">
            <p>{products.length} бүтээгдэхүүн олдлоо</p>
          </div>

          <ProductList products={products} loading={loading} error={error} />
        </main>
      </div>
    </div>
  );
};

export default ProductsPage;
