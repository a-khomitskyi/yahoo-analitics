CREATE TABLE ZM (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT zm_pk PRIMARY KEY (Date)
    );
CREATE TABLE ZUO (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT zuo_pk PRIMARY KEY (Date)
    );
CREATE TABLE DOCU (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT docu_pk PRIMARY KEY (Date)
    );
CREATE TABLE PD (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT pd_pk PRIMARY KEY (Date)
    );
CREATE TABLE PINS (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT pins_pk PRIMARY KEY (Date)
    );
CREATE TABLE CLDR (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT cldr_pk PRIMARY KEY (Date)
    );
CREATE TABLE RUN (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume INT,
    CONSTRAINT run_pk PRIMARY KEY (Date)
    );