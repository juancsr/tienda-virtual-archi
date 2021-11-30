export const querys = {
  createTable:"CREATE TABLE IF NOT EXISTS Products ("+
                                                      "Id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                                                      "Name TEXT,"+
                                                      "Description TEXT,"+
                                                      "Quantity INTEGER"+
                                                      
                                                      ");",
  getAllProducts: "SELECT * FROM Products",
  getProducById: "SELECT * FROM Products Where Id = ?",
  addNewProduct:
    "INSERT INTO Products (name, description, quantity) VALUES (@name,@description,@quantity);",
  deleteProduct: "DELETE FROM Products WHERE Id = ?",
  getTotalProducts: "SELECT COUNT(*)Cantidad FROM Products",
  updateProductById:
    "UPDATE Products SET Name = @name, Description = @description, Quantity = @quantity WHERE Id = @id",
};
