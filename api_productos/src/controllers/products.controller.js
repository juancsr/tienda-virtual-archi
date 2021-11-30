import { getConnection, querys, sql } from "../database";


export const createTable = async() => {
    try {
        const pool = await getConnection();
        const result = await pool.run(querys.createTable);
        console.log(result.recordset);
    } catch (error) {
        res.status(500);
        console.log(error.message);
    }
};
export const getProducts = async(req, res) => {
    try {
        const pool = await getConnection();
        let data=Array();
        await pool.all(querys.getAllProducts,function(err,row)
        {
            //console.log(row);
            res.status(200).json(row);
            
        });
    } catch (error) {
        res.status(500);
        console.log(error);
        res.send(error.message);
    }
};

export const createNewProduct = async(req, res) => {
    const { name, description } = req.body;
    let { quantity } = req.body;

    // validating
    if (description == null || name == null) {
        return res.status(400).json({ msg: "Bad Request. Please fill all fields" });
    }

    if (quantity == null) quantity = 0;

    try {
        const pool = await getConnection();

        await pool
            .run(querys.addNewProduct,[name,description,quantity],function(err,row){
                console.log(`A row has been inserted with rowid ${this.lastID}`);
                res.json({"Id":`${this.lastID}`,"name":name, "description":description,"quantity":quantity});
            });
            //.input("name", sql.VarChar, name)
            //.input("description", sql.Text, description)
            //.input("quantity", sql.Int, quantity)
            //.query(querys.addNewProduct);

        //res.json({ name, description, quantity });
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

export const getProductById = async(req, res) => {
    try {
        const pool = await getConnection();

        /*const result = await pool
            .request()
            .input("id", req.params.id)
            .query(querys.getProducById);*/
            console.log(req.params);
        await pool.get(querys.getProducById,[req.params.id],function(err,row)
        {
            res.json({"Id":row.Id,"name":row.Name, "description":row.Description,"quantity":row.Quantity});
        });
        //return res.json(result.recordset[0]);
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

export const deleteProductById = async(req, res) => {
    try {
        const pool = await getConnection();

        /*const result = await pool
            .request()
            .input("id", req.params.id)
            .query(querys.deleteProduct);*/
            await pool.run(querys.deleteProduct,[req.params.id],function(err,row)
            {
                res.status(200).json(row);
            });
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};

export const getTotalProducts = async(req, res) => {
    const pool = await getConnection();

    await pool.get(querys.getTotalProducts,[],function(err,row)
            {
                return res.status(200).json(row);
            });
};

export const updateProductById = async(req, res) => {
    const { description, name, quantity } = req.body;

    // validating
    if (description == null || name == null || quantity == null) {
        return res.status(400).json({ msg: "Bad Request. Please fill all fields" });
    }

    try {
        const pool = await getConnection();
        await pool.run(querys.updateProductById,[name,description,quantity,req.params.id],function(err,row)
            {
                return res.status(200).json({"id":`${req.params.id}`,"name":name,"description":description,"quantity":quantity});
            });
        /*
        await pool
            .request()
            .input("name", sql.VarChar, name)
            .input("description", sql.Text, description)
            .input("quantity", sql.Int, quantity)
            .input("id", req.params.id)
            .query(querys.updateProductById);
        res.json({ name, description, quantity });*/
        
    } catch (error) {
        res.status(500);
        res.send(error.message);
    }
};
