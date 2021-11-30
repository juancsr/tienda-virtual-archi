import { Router } from "express";
import {
    getProducts,
    createNewProduct,
    getProductById,
    deleteProductById,
    getTotalProducts,
    updateProductById,
    createTable,
} from "../controllers/products.controller";
createTable();
const router = Router();

router.get("/products", getProducts);

router.post("/products", createNewProduct);

router.get("/products/count", getTotalProducts);

router.get("/products/:id", getProductById);

router.delete("/products/:id", deleteProductById);

router.put("/products/:id", updateProductById);

export default router;
