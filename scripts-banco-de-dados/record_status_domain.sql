CREATE DOMAIN public.record_status
    AS smallint
    DEFAULT 1
    NOT NULL;

ALTER DOMAIN public.record_status OWNER TO postgres;

ALTER DOMAIN public.record_status
    ADD CONSTRAINT check_record_status CHECK (VALUE = ANY (ARRAY[0, 1, 2]));

COMMENT ON DOMAIN public.record_status
    IS '0=Inactive, 1=Active, 2=Deleted';