configurations = \
{0: {'model_name': "ARD-VAE",
     'dataset_name': "CIFAR10",
     'batch_size': 100,
     'epochs': 100,
     'latent_dim': 256,
     'num_filter': 128,
     't_stat_samples': 10000,
     'update_hyperpriors': 1,  # "iterations to update the t-distribution parameters"
     'update_t_stat_epoch_fraction': 1,  # "epochs to shuffle training samples"
     'print_every_epoch': 1,
     'save_every_epoch': 10,
     'dec_reg_strength': 0,
     'learning_rate': 5e-04,
     'patience': 10,                     # "patience window for the LR schedular"
     'factor': 0.5,                      # "reduce the learning rate by 0.5 beyond the patience window"
     'encoder_use_batch_norm': True,
     'decoder_use_batch_norm': True,
     'scatter_use_var': True,
     'shuffle_scatter_samples': True,
     'train_data_noise': False,
     'train_from_checkpoint': False,
     'print_model_summary': False,
     'conv_kernel_initializer_method': 'he_normal',
     'kld_scalar': 0.05,
     'fid_samples': 10000,
     },
1: {'model_name': "ARD-VAE",
     'dataset_name': "CelebA",
     'batch_size': 100,
     'epochs': 50,
     'latent_dim': 64,
     'num_filter': 64,
     't_stat_samples': 10000,
     'update_hyperpriors': 1,  # "iterations to update the t-distribution parameters"
     'update_t_stat_epoch_fraction': 1,  # "epochs to shuffle training samples"
     'print_every_epoch': 1,
     'save_every_epoch': 10,
     'dec_reg_strength': 0,
     'learning_rate': 5e-04,
     'patience': 10,                     # "patience window for the LR schedular"
     'factor': 0.5,                     # "reduce the learning rate by 0.5 beyond the patience window"
     'encoder_use_batch_norm': True,
     'decoder_use_batch_norm': True,
     'scatter_use_var': True,
     'shuffle_scatter_samples': True,
     'train_data_noise': False,
     'train_from_checkpoint': False,
     'print_model_summary': False,
     'conv_kernel_initializer_method': 'he_normal',
     'kld_scalar': 3.0,
     'fid_samples': 10000,
    },
 2: {'model_name': "ARD-VAE",
     'dataset_name': "MNIST",
     'batch_size': 100,
     'epochs': 50,
     'latent_dim': 128,
     'num_filter': 64,
     't_stat_samples': 10000,
     'update_hyperpriors': 1,  # "iterations to update the t-distribution parameters"
     'update_t_stat_epoch_fraction': 1,  # "epochs to shuffle training samples"
     'print_every_epoch': 1,
     'save_every_epoch': 10,
     'dec_reg_strength': 0,
     'learning_rate': 5e-04,
     'patience': 10,  # "patience window for the LR schedular"
     'factor': 0.5,  # "reduce the learning rate by 0.5 beyond the patience window"
     'encoder_use_batch_norm': True,
     'decoder_use_batch_norm': True,
     'scatter_use_var': True,
     'shuffle_scatter_samples': True,
     'train_data_noise': False,
     'train_from_checkpoint': False,
     'print_model_summary': False,
     'conv_kernel_initializer_method': 'he_normal',
     'kld_scalar': 0.5,
     'fid_samples': 10000,
    },
 },