## Try Django deployment to Vercel



optimize PostgreSQL's settings:

 ALTER ROLE <myuser> SET client_encoding TO 'utf8';
 ALTER ROLE <myuser> SET default_transaction_isolation TO 'read committed';
 ALTER ROLE <myuser> SET timezone TO 'UTC';
