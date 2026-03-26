const express = require("express");
const router = express.Router();
const products = require("../data/products");

router.get("/", (req, res) => {
  res.json(products);
});

router.post("/", (req, res) => {
  const { name, price } = req.body;
  const product = {
    id: products.length + 1,
    name,
    price
  };
  products.push(product);
  res.status(201).json(product);
});

router.put("/:id", (req, res) => {
  const productId = Number(req.params.id);
  const product = products.find((p) => p.id === productId);

  if (!product) {
    return res.status(404).json({ error: "Product not found" });
  }

  product.name = req.body.name ?? product.name;
  product.price = req.body.price ?? product.price;
  res.json(product);
});

router.delete("/:id", (req, res) => {
  const productId = Number(req.params.id);
  const index = products.findIndex((p) => p.id === productId);

  if (index === -1) {
    return res.status(404).json({ error: "Product not found" });
  }

  const removed = products.splice(index, 1)[0];
  res.json(removed);
});

module.exports = router;
